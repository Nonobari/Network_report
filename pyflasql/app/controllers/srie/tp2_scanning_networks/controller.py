# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Implements the logic for TP2 - Scanning Networks
"""
from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from ....models.sql import db, UserDB
from ...utils import get_shell_output
from ....models.srie.tp2_scanning_networks.forms import PingAddrForm
from ....models.srie.tp2_scanning_networks.forms import NmapForm
from ....models.srie.tp2_scanning_networks.forms import DnsReconForm
from ....models.srie.tp2_scanning_networks.forms import DnsEnumForm, TraceRouteForm


@login_required
def srie_tp2_scanning_networks():
    """
        Logic for /srie/tp2_scanning_networks/home
        Login is required to view this page

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networks/home.html
        """
    username = current_user.username
    return render_template(url_for('blueprint.srie_tp2_scanning_networks')+'.html', username=username)

@login_required
def srie_tp2_pingaddr():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/pingaddr.html
        Login is required to view this page

        Print in the user interface private and public IP addresses.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/pingaddr.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": PingAddrForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        ip_address = content["form"].ip_address.data
        npings = content["form"].npings.data
        content["command_executed"] = f"ping -c {npings} {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_pingaddr')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_pingaddr')+'.html', content=content)

@login_required
def srie_tp2_Nmap():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/Nmap.html
        Login is required to view this page

        Scan network with Nmap

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/Nmap.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": NmapForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        ip_address = content["form"].ip_address.data
        scan_type = content["form"].scan_type.data
        ports = content["form"].ports.data

        content["command_executed"] = f"nmap -{scan_type} -p {ports} {ip_address}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_Nmap')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_Nmap')+'.html', content=content)

@login_required
def srie_tp2_DnsRecon():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/DnsRecon.html
        Login is required to view this page

        DNSRecon is a widely used Python script that provides comprehensive DNS enumeration capabilities for a domain.s.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/DnsRecon.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": DnsReconForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        domain = content["form"].domain.data

        content["command_executed"] = f"dnsrecon -d {domain}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_DnsRecon')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_DnsRecon')+'.html', content=content)

@login_required
def srie_tp2_DnsEnum():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/DnsEnum.html
        Login is required to view this page

        DNSRecon is a widely used Python script that provides comprehensive DNS enumeration capabilities for a domain.s.

        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/DnsEnum.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": DnsEnumForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        # Get IP address and number of pings from the user interface (UI)
        domain = content["form"].domain.data

        content["command_executed"] = f"dnsenum -w {domain}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_DnsEnum')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_DnsEnum')+'.html', content=content)


@login_required
def srie_tp2_TraceRoute():
    """
        Handles the logic for view/templates/srie/tp2_scanning_networds/TraceRoute.html
        Login is required to view this page

        Traceroute is a network diagnostic tool that traces the route taken by IP packets to a specific network or internet host. It reveals the sequence of intermediate machines or routers the packets pass through, along with their IP numbers and host names (if available). This information helps in identifying the network hops taken by the packets, pinpointing potential issues or delays, and aiding in network troubleshooting and optimization.
        Args:
            - None.

        Returns:
            - rendered template view/templates/srie/tp2_scanning_networds/TraceRoute.html with content passed as a context variable
        """
    # Create a dict to store the formulary and the shell output. This dict is passed to the .html file.
    content = {"form": TraceRouteForm(),
               "command_executed": "Waiting ...",
               "command_output": "Waiting ..."
               }
    
    if content["form"].validate_on_submit():
        
        domain = content["form"].domain.data

        content["command_executed"] = f"traceroute {domain}"
        content["command_output"] = get_shell_output(content["command_executed"])
        # print(content["shell_output"])  # for debug only
        return render_template(url_for('blueprint.srie_tp2_TraceRoute')+'.html', content=content)

    return render_template(url_for('blueprint.srie_tp2_TraceRoute')+'.html', content=content)