# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP4 - Gaining Access
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp4_gaining_access.forms import hydraForm, sqlmapForm


@login_required
def srie_tp4_gaining_access():
    """
        Logic for /srie/tp4_gaining_access/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp4_gaining_access')+'.html', username=username)

@login_required
def srie_tp4_hydra():
    """
        Handles the logic for view/templates/srie/tp4_gaining_access/hydra.html
        Login is required to view this page

        Hydra is a parallelized login cracker which supports numerous protocols to attack. New modules are easy to add, beside that, it is flexible and very fast.
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/hydra.html with content passed as a context variable
        """
    content = {"form": hydraForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        loginPath = content["form"].loginPath.data
        passPath = content["form"].passPath.data
        host = content["form"].host.data
        service = content["form"].service.data
        content["command_executed"] = f"hydra -L {loginPath} -P {passPath} {host} {service} -V"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp4_hydra')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp4_hydra')+'.html', content=content)

@login_required
def srie_tp4_sqlmap():
    """
        Handles the logic for view/templates/srie/tp4_gaining_access/sqlmap.html
        Login is required to view this page

        sqlmap is an automatic SQL injection tool.
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp4_gaining_access/sqlmap.html with content passed as a context variable
        """
    content = {"form": sqlmapForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        url = content["form"].url.data
        content["command_executed"] = f"sqlmap -u {url} --batch"
        content["command_output"] = get_shell_output(content["command_executed"])
        
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp4_sqlmap')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp4_sqlmap')+'.html', content=content)