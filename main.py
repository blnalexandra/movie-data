
from filmapp.repository.Repository import Repository
from filmapp.service.Service import Service
from filmapp.ui.UI import UI

repository = Repository()
service = Service(repository)
ui = UI(service)
ui.program()
