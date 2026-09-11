---
title: "만들다 멈춘 SessionCue, 그리고 iTerm2의 Claude Code 통합"
summary: "여러 에이전트 세션의 상태를 모아보려고 만들던 SessionCue를 보류한 뒤, iTerm2의 Claude Code 연동을 써보며 직접 만들고 유지할 이유를 다시 생각했습니다."
slug: sessioncue-iterm2-integration
format: essay
tags: ["ai-agent", "developer-tools", "iterm2", "sessioncue"]
series: []
toc: false
date: 2026-09-11
og_image: iterm2-claude-integration.png
draft: false
---

전에 만들다 보류해 둔 작은 도구가 있습니다. SessionCue입니다.

Claude Code와 Codex 세션을 여러 개 켜 놓으면, 어느 세션이 승인이나 입력을 기다리는지 놓치기 쉬웠습니다. 일을 시켜 둔 세션이 작업 중인지, 응답을 기다리며 멈춰 있는지 확인하려 터미널을 오가곤 했습니다.

SessionCue는 그 불편을 줄이려고 만들던 macOS 메뉴 막대 앱입니다. 여러 도구의 세션 상태를 모아 지금 확인해야 할 세션을 알려주는 것이 목표였습니다. 에이전트를 실행하거나 지휘하는 기능보다는, 확인이 필요한 순간을 알려주는 데 집중했습니다. iTerm2와 연동하는 방향도 고민했습니다.

그러다 에이전트 도구들이 발전하는 방향을 보며, 조금 더 지켜보는 편이 낫겠다는 생각이 들었습니다. 개발은 잠시 멈춰두었습니다.

그렇게 보류해 둔 상태에서 2026년 9월 11일, iTerm2의 Claude Code 연동을 직접 설정했습니다. 화면을 보고 나니 개발을 멈춰두길 잘했다는 생각이 들었습니다.

![iTerm2의 Claude Code Workgroup과 Session Status 패널](/posts/sessioncue-iterm2-integration/iterm2-claude-integration.png)

*직접 설정한 iTerm2 화면입니다. 오른쪽 Session Status에 두 Claude 세션의 idle 상태가 표시되어 있습니다.*

iTerm2는 9월 8일 출시한 3.7 정식 버전의 주요 기능으로 Claude Code 통합을 소개했습니다. 베타에서 제공하던 기능이 정식 버전에 들어온 것입니다. [정식 출시 안내](https://iterm2.com/news.html), [베타 릴리스 기록](https://github.com/gnachman/iTerm2/blob/master/docs/notes-3.7.0beta2.txt)

설정은 iTerm2 메뉴의 ‘Install Claude Code Integration’에서 시작합니다. 안내에 따라 Python API를 활성화하고, Claude의 상태를 전달하는 Hook과 관련 화면을 묶는 Workgroup 등을 설정합니다. 자동 진입을 켜두면 선택한 터미널 프로필에서 `claude`를 실행할 때 작업 화면이 함께 열립니다. [공식 설치 안내](https://iterm2.com/claude-code-integration.html)

상단에서는 Chat·Diff·Code Review를 오갈 수 있습니다. Claude와 대화하다가 코드 변경 사항을 확인하고, 별도 세션에서 리뷰를 요청하는 구성입니다. 이처럼 관련 세션을 한곳에 묶어두는 기능을 iTerm2에서는 Workgroups라고 부릅니다. [Workgroups 설명](https://iterm2.com/documentation-workgroups.html)

특히 눈에 들어온 것은 오른쪽 Session Status였습니다. 작업 중인 세션, 승인이나 입력이 필요한 세션, 작업을 마치고 다음 요청을 기다리는 세션을 모아서 보여줍니다. 응답이 필요한 세션이 위로 올라오고, 클릭하면 해당 세션으로 이동합니다. SessionCue로 해결하려던 문제와 직접 맞닿아 있는 부분입니다. [Session Status 설명](https://iterm2.com/documentation-session-status.html)

물론 기능의 범위를 구분할 필요는 있습니다. 설치 메뉴가 제공하는 연동은 Claude Code용입니다. Workgroups 자체는 다른 CLI를 실행하도록 구성할 수 있는 범용 기능이지만, 각 도구의 작업 상태까지 표시하려면 그 상태를 iTerm2에 전달하는 연결이 필요합니다. 이 화면만으로 Claude Code와 Codex를 함께 다루려던 SessionCue의 목표가 전부 충족됐다고 보기는 어렵습니다. [연동 범위](https://iterm2.com/claude-code-integration.html), [상태 연결 방식](https://iterm2.com/documentation-session-status.html)

그럼에도 직접 앱을 만들어 유지해야 할 이유는 줄어들었습니다. 평소 쓰던 터미널 안에서 불편의 상당 부분을 해결할 수 있게 되었기 때문입니다. 다만 실제 사용에 앞서 보안 설정과 데이터가 전달되는 범위는 충분히 확인할 필요가 있습니다.

이 경험을 통해 작은 개발 도구를 만들 때 어디까지 직접 구현할 것인지 다시 생각하게 되었습니다.

당장 겪는 불편은 좋은 출발점입니다. SessionCue도 실제로 겪던 문제에서 시작했습니다. 다만 그 불편을 해결하기 위해 별도 앱을 계속 개발해야 하는지는 별개의 문제입니다. 이미 쓰고 있는 도구가 비슷한 기능을 제공한다면, 먼저 사용해 보고 어떤 불편이 남는지 확인할 필요가 있습니다.

별도 앱을 만들면 계속 챙겨야 할 일이 생깁니다. 각 에이전트가 상태를 전달하는 방식이 바뀌면 연결을 점검해야 하고, 오래된 상태가 화면에 남아 사용자가 현재 상태로 오해하지 않도록 관리해야 합니다. 설치와 업데이트가 문제없이 이루어지는지도 챙겨야 합니다. 작은 상태 패널 하나라도 믿고 쓰게 만들려면 화면을 구현하는 것 외에도 할 일이 많습니다.

그래서 지금은 '이미 만든 코드의 양'보다 '앞으로도 이 도구를 별도로 유지할 이유가 얼마나 남아 있는가'를 기준으로 판단하려 합니다.

기존 도구를 설정하는 것으로 충분한지, 도구 사이에 작은 연결을 추가하면 되는지, 별도 앱이 있어야만 해결되는 불편이 남아 있는지를 먼저 살펴보려 합니다. SessionCue에 추가할 수 있는 기능은 더 있겠지만, 기능을 더 만들 수 있다는 사실만으로 개발을 계속해야 하는 것은 아닐 것입니다.

이번 경험 하나로 AI 개발 도구 시장 전체를 설명할 수는 없습니다. 다만 해결하려던 문제가 터미널 안에서 다뤄지기 시작했다는 점은, 시간과 노력을 어디에 쓸지 판단하는 데 충분히 의미 있는 변화였습니다.

![실제 Claude Code와 Codex 세션 상태를 표시한 SessionCue 개발 화면](/posts/sessioncue-iterm2-integration/sessioncue-live-sessions.png)

*Claude Code와 Codex의 실제 세션을 연결한 SessionCue 0.0.1 알파의 개발 화면입니다. 승인 대기·실행 중·완료 상태를 함께 띄웠습니다. 촬영을 위해 메뉴 막대와 동일한 UI를 별도 창에서 열었습니다.*

SessionCue는 보류 상태로 두려 합니다. 만들어 둔 화면은 기록으로 남깁니다.

앞으로는 평소 쓰던 환경에서 응답을 기다리는 세션을 얼마나 잘 파악할 수 있는지 살펴보려 합니다.
