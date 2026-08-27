---
title: "AI로 코딩하는 사람을 위한 Git"
slug: learnstead-ai-coding-git-guide
format: note
tags: ["learnstead", "git", "ai-coding", "worktree"]
series: ["Learnstead 가이드"]
summary: "AI가 만든 변경을 저장·확인·분리·공유하고, branch와 worktree로 여러 AI 작업을 안전하게 나누는 Learnstead Git 가이드 소개."
toc: true
date: 2026-08-27
edited: false
og_image: git-for-vibe-coders-hero-social.webp
provenance_note: "이 글은 첫 공개 초안입니다."
---

AI 코딩 도구는 짧은 시간에 여러 파일을 바꿉니다. 그래서 코드를 만드는 속도보다 먼저 필요한 것이 있습니다.

> 무엇이 바뀌었고, 어디까지 되돌릴 수 있으며, 어떤 결과를 남길지는 누가 결정할까?

그 결정은 사람이 해야 합니다. Git은 그 판단에 필요한 기록과 경계를 만듭니다. 잘 동작하는 상태를 commit으로 남기고,
AI가 만든 diff를 확인하고, 서로 다른 시도를 branch로 분리할 수 있습니다.

Learnstead의 새 가이드 「AI로 코딩하는 사람을 위한 Git」은 Git이 처음인 사람도 AI와 작업하며 변경의 결정권을 유지할 수
있도록 구성한 자료입니다. 명령어를 외우는 대신 각 명령이 무엇을 바꾸고, 언제 멈춰야 하는지를 이해하는 데 초점을 맞췄습니다.

![한 프로젝트의 변경을 Git에 저장하고 main과 worktree의 별도 작업 공간으로 나눈 뒤 검토한 결과만 합치는 Learnstead Git 가이드 삽화](git-for-vibe-coders-hero-social.webp)

## AI와 코딩할수록 Git을 알아야 하는 이유

Git은 여러 개발자가 협업할 때만 쓰는 도구가 아닙니다. AI가 바꾼 파일을 검토하고 필요한 부분만 되돌리며, 확인한 결과만
남기는 데도 필요합니다. 가이드는 이 흐름을 네 단계로 정리합니다.

- **Save** — 돌아갈 수 있는 상태를 commit으로 남깁니다.
- **Inspect** — `status`와 `diff`로 AI가 바꾼 파일과 줄을 확인합니다.
- **Isolate** — branch와 worktree로 서로 다른 시도를 분리합니다.
- **Share** — 검토한 commit만 원격에 올리고 PR과 공개 단계를 나눕니다.

Git 명령 실행 자체는 AI에게 맡길 수 있습니다. 다만 어떤 변경을 저장할지, 무엇을 버릴지, 어느 branch를 합칠지, 언제 외부에
공개할지는 사용자가 확인하고 승인해야 합니다.

## branch는 갈래이고, worktree는 책상을 늘린다

branch와 worktree는 비슷해 보이지만 역할이 다릅니다. branch는 commit 기록이 이어질 **작업의 갈래입니다.** 기본 작업
폴더에서는 `git switch`로 branch를 바꿀 때 펼쳐진 파일도 함께 바뀝니다.

책상에 비유하면 branch를 바꾸는 것은 **같은 책상 위에 펼친 책을 바꾸는 일입니다.** worktree는 **책상을 하나 더 놓는
일입니다.** 새 책상마다 서로 다른 branch를 펼쳐 둘 수 있어, 한 AI가 기능을 만드는 동안 다른 AI가 오류를 고치거나 두 구현안을
동시에 실행해 비교할 수 있습니다.

![공용 Git 저장소의 기록을 공유하면서 branch는 한 책상에서 펼친 작업을 바꾸고, worktree는 책상을 추가해 여러 branch를 동시에 펼치는 비교](git-branch-vs-worktree.svg)

worktree는 저장소를 새로 복제하는 clone이 아닙니다. 각 작업 폴더의 수정 파일과 staging 상태는 분리되지만 commit·branch 기록과
remote 설정은 공유합니다. 폴더를 나눈다고 merge 충돌까지 없어지는 것도 아닙니다. 같은 줄을 다르게 고쳤다면 나중에 합칠 때 여전히
충돌할 수 있습니다.

가이드에서는 AI 세션 하나에 worktree 하나와 branch 하나를 배정하고, 각 세션의 범위·성공 판정·commit을 따로 확인한 뒤 main에
합치는 흐름까지 다룹니다.

## 안전한 명령과 멈춰야 할 명령을 구분했다

`git status`처럼 상태만 읽는 명령과 `git add`처럼 staging 상태를 바꾸는 명령, 작업을 잃을 수 있는 명령은 위험이 다릅니다. 그래서
가이드 마지막에는 AI에게 복사해 쓸 수 있는 작업 지시문과 Git 명령 신호등을 함께 넣었습니다.

실습에서는 다음 상황을 직접 만들고 결과를 확인했습니다.

- 파일 세 개 중 하나만 `git restore`로 되돌리고 나머지 변경이 유지되는지 확인했습니다.
- `git reset --hard HEAD`가 Git이 추적하는 파일의 미커밋 변경을 실제로 없애는 것을 확인했습니다.
- `main`과 새 branch를 두 worktree에 동시에 열고, 작업 파일과 staging 상태가 분리되는지 확인했습니다.
- `.env`가 staging과 commit에 들어간 상황에서 push 전에 빼는 절차를 확인했습니다.
- 두 branch가 같은 줄을 고쳐 merge 충돌이 나는 상황을 만들고 해결했습니다.

이 실행 기록은 macOS 26.6.2와 Git 2.50.1 환경에서 확인했습니다. Windows 설치와 Git Bash 경로, 실제 GitHub 계정으로
진행하는 push·PR, 저장소 공개와 release는 공식 문서와 공개 가이드를 대조한 범위이며 직접 실행 검증으로 표시하지 않았습니다.

## 어디서 시작하면 좋을까

[Learnstead 저장소](https://github.com/kyungseo/learnstead)에 접속해 세 번째 카드의 ‘가이드 시작 →’를 누르면 됩니다.
Git이 처음이라면 [10분 안에 첫 저장 지점](https://github.com/kyungseo/learnstead/blob/main/guides/git-for-vibe-coders/README.md#가장-짧은-경로--10분-안에-첫-저장-지점)부터,
여러 AI 작업을 동시에 나누고 싶다면 [worktree 장](https://github.com/kyungseo/learnstead/blob/main/guides/git-for-vibe-coders/07-worktrees.md)부터
읽을 수 있습니다.

전체 가이드는 version control의 시작부터 Git과 GitHub의 차이, 네 작업 공간, commit과 되돌리기, branch·worktree·PR, Secret
파일 사고 대응과 공개 전 점검까지 13개 문서로 이어집니다.

<!-- 글 하단 기록은 site가 front matter에서 자동 렌더. -->
