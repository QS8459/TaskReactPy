import os;
import json;

from src.config import BOOTSTRAP_CSS, BOOTSTRAP_SCRIPT, LOCAL_STYLE;
from src.service import TaskAPI;

client = TaskAPI();

from fastapi import FastAPI;

from reactpy import component, html;
from reactpy_router import route, simple;
from reactpy.backend.fastapi import configure;
from src.components import Comps;
from src.pages import Pages;
comps = Comps()
pages = Pages();


@component
def root():
    return simple.router(
            route("/home",pages.home()),
            route('/signin', pages.login()),
            route('/task', pages.addTask()),
            route('/task/list', comps.taskList()),
            route('/test', comps.test()),
            route("*", html.h1("Missing Link %%%"))
        );

app = FastAPI();

configure(app, root);

