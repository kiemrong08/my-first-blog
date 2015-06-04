@ECHO OFF
git status
@PAUSE
git add -A .
@PAUSE
git status
@PAUSE
git commit -m "Added views to create/edit blog post inside the site."
@PAUSE
git push
@PAUSE