# Software Project

### Installation
```bash
$ git clone https://github.com/m3hransh/software_project.git
$ pip install -r requirements.txt
```
### Execuation
```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

#### Currents Routs
* **'/':**: Dashboard for the staffs
* **'/form/\<section>'**: Registering different services base on section
* **'/login'**: Loging page for the staffs

### Contribution
```bash
$ git clone https://github.com/m3hransh/software_project.git
$ git checkout -b 'Data-representation'
# Do your work
$ git add -all
$ git commit -m '<commit_message>'
# Make sure your repository is updated
$ git pull --rebase
$ git push origin 
```


### To-Do
- [ ] compelete tracking page
- [ ] tracking page for the users
- [ ] Data representation
- [ ] make structure using blueprint and seperate model classes