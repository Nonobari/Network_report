# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP1 - Reconnaissance Footprint
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output, CheckIf
from ....models.srie.tp1_recon_footprint.forms import WhoisForm
from ....models.srie.tp1_recon_footprint.forms import theHarvesterForm
from ....models.srie.tp1_recon_footprint.forms import HoleheForm
import importlib

@login_required
def srie_home():
    """
        Handles the logic for /srie/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_home')+'.html', username=username)

@login_required
def srie_tp1_recon_footprint():
    """
        Handles the logic for /srie/tp1_recon_footprint/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/home.html with the username passed as a context variable
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp1_recon_footprint')+'.html', username=username)

@login_required
def srie_tp1_ipaddr():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/ipaddr.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/ipaddr.html with content passed as a context variable
        """
    # Create a dictionary to store the private and public IP addresses
    content = {"ip_address_private": "x.x.x.x", 
               "ip_address_public": "x.x.x.x",
               "cmd_ip_address_private": f"hostname -I",
               "cmd_ip_address_public": f"To be implemented"
               }
    # Uses get_shell_output() to execute a command in the shell and store the output in the dict.
    content["ip_address_private"] = get_shell_output(content["cmd_ip_address_private"])
    content["ip_address_public"]  = get_shell_output(content["cmd_ip_address_public"])
    return render_template(url_for('blueprint.srie_tp1_ipaddr')+'.html', content=content)



@login_required
def srie_tp1_whois():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/whois.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/whois.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": WhoisForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        domain = content["form"].domain.data
        content["command_executed"] = f"curl -s https://raphaelviera.fr/ismin/toolbox/whois/whois.php?domain={domain}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_whois')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_whois')+'.html', content=content)

@login_required
def srie_tp1_theHarvester():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/theHarvester.html
        Login is required to view this page

        theHarvester is used to gather open source intelligence (OSINT) on a company or domain.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/theHarvester.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": theHarvesterForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        domain = content["form"].domain.data
        limite = content["form"].limite.data
        source = content["form"].source.data
        content["command_executed"] = f"theHarvester -d {domain} -l {limite} -b {source}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_theHarvester')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_theHarvester')+'.html', content=content)

@login_required
def srie_tp1_Holehe():
    """
        Handles the logic for view/templates/srie/tp1_recon_footprint/Holehe.html
        Login is required to view this page

        Holehe checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp1_recon_footprint/Holehe.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": HoleheForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
   
        email = content["form"].email.data
        # Check if holehe is already installed
        try:
            importlib.import_module("holehe")
        except ImportError:
        # holehe is not installed, run pip3 install command
            content["command_executed"] = f"pip3 install holehe && holehe {email}"
            content["command_output"] = get_shell_output(content["command_executed"])
        else:
        # holehe is already installed, skip pip3 install command
            content["command_executed"] = f"holehe {email}"
            content["command_output"] = get_shell_output(content["command_executed"])
        
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp1_Holehe')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp1_Holehe')+'.html', content=content)
