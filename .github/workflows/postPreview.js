const fs = require('fs');

export default function(github, context) {
    const preview = fs.readFileSync('../docs/index.md').toString();
    github.issues.createComment({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: preview
      })
}