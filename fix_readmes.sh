#!/bin/bash

# Fix the duplicate gemini code blocks in README_zh.md
sed -i '' '/```bash/,/```/!b;//!d;/```bash/!d' README_zh.md
