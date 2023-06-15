# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP3 - Enumeration
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp3_enumeration.forms import TelnetForm, Enum4linuxForm


@login_required
def srie_tp3_enumeration():
    """
        Logic for /srie/tp3_enumeration/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp3_enumeration')+'.html', username=username)

@login_required
def srie_tp3_Telnet():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/Telnet.html
        Login is required to view this page

        The telnet command is a networking protocol used for establishing an interactive communication session with another host via the TELNET protocol. This protocol enables a user to access and communicate with a remote computer as if they were physically present at the remote location.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/Telnet.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TelnetForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data
        port = content["form"].port.data

        content["command_executed"] = f"telnet {host} {port}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_Telnet')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_Telnet')+'.html', content=content)

@login_required
def srie_tp3_Netcat():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/Netcat.html
        Login is required to view this page

        Netcat is a simple Unix utility which reads and writes data across network connections using TCP or UDP protocol. It is designed to be a reliable “back-end” tool that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and exploration tool, since it can create almost any kind of connection you would need and has several interesting built-in capabilities.

        I use the same form as TelnetForm
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/Netcat.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TelnetForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data
        port = content["form"].port.data

        content["command_executed"] = f"netcat {host} {port}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_Netcat')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_Netcat')+'.html', content=content)

@login_required
def srie_tp3_Enum4linux():
    """
        Handles the logic for view/templates/srie/tp3_enumeration/Enum4linux.html
        Login is required to view this page

        Enum4linux is used to enumerate Windows and Samba hosts. Below are the most common options used in enum4linux. 

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp3_enumeration/Enum4linux.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": Enum4linuxForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        host = content["form"].host.data

        content["command_executed"] = f"enum4linux -U {host}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp3_Enum4linux')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp3_Enum4linux')+'.html', content=content)