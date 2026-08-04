---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
slug: "{{ .File.ContentBaseName }}"
date: {{ .Date }}
draft: true
format: essay        # essay | note
tags: []
series: []           # 시리즈 slug — 없으면 빈 배열
summary: ""
toc: false
# 재게시·개작일 때만:
# original_date:
# original_url:
# edited: false
# 게시 후 social 배포 시:
# social_url:
---
