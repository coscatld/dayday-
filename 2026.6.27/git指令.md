流程一：基础分支合并流
1.切换到开发分支：git checkout develop（如果分支不存在，用 git checkout -b develop 创建并切换）
2.暂存代码：git add .（推荐用点号代替星号，点号会包含所有的隐藏文件）
3.提交代码：git commit -m "feat: 完成了某个新功能"
4.切换回主干分支：git checkout main
5.合并代码：git merge develop（将 develop 分支合并到当前的 main 分支）
6.送快递：git remote add origin [仓库地址]
7.推送代码：git push origin main
8.拉取合并：git pull origin main --allow-unrelated-histories


扩展：日常必备 Git 命令速查表

一、状态与记录查看
git status：查看当前工作区状态（哪些文件改了，哪些在暂存区）。
git log：查看详细的提交历史记录（按 q 退出）。
git log --oneline --graph：以更简洁、图形化的方式查看历史和分支走向。

二、分支管理 
git branch：列出本地所有分支，当前分支前面会有 * 号。
git branch -a：查看本地和远程的所有分支。
git branch -d 分支名：删除本地分支。
git branch -D 分支名：强制删除本地分支（危险操作，确认代码不要了再用）。

三、撤销与回退
git checkout -- 文件名：撤销工作区的修改（代码写乱了，恢复到上次 commit 的状态）。
git reset HEAD 文件名：把文件从暂存区撤回（git add 错了，但不想丢失修改的代码）。
git reset --hard HEAD^：彻底回退到上一个版本（连代码修改都不要了，极其危险，慎用）。

四、暂存工作现场
git stash：把当前还没 commit 的代码像草稿纸一样存起来，让工作区变得干净。
git stash list：查看存了多少张草稿。
git stash pop：修完紧急 Bug 回来后，把最近一次存的草稿恢复到工作区继续开发。
