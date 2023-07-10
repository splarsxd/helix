@echo off
color c
title ping open
cls

mode con: cols=60 lines=3
:: original ipv4 address changed, 2023-06-25 | 15:48, this new ipv4 address redirects to cloudflare timeouts.
:: ping open.90gq.se -t
ping 90gqopen.se -t