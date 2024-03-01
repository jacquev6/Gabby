*Opinion* is a very opinionated template for web applications.

It's designed to be used as a vendor branch and minimize conflicts on update if you follow these guidelines:
- never modify a file with `opinion` in its name
- never modify a file inside a directory with `opinion` in its name
- for each file named `*.opinion.template`, create a file:
  - named like the template without the `.opinion.template` suffix
  - following the instructions in the template file
- modify files with `app` in their name as you see fit
- avoid modifying other files provided by *Opinion* if possible
