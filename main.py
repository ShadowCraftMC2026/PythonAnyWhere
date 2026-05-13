import os
import sys
import time
import random
from threading import Thread
from flask import Flask
import discord
from discord import app_commands
from discord.ext import commands

# ==============================================================================
# PROJECT MANIFEST: PythonAnyWhere (Own By ShadowCraftMC, PythonAnyWhere)
# ARCHITECTURE: Dual-Engine Concurrency Framework (Web Keep-Alive + Discord API)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. 24/7 CLOUD PERSISTENCE ENGINE (Flask Web Server Network Core)
# ------------------------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def live_traffic_endpoint():
    """Serves the HTTP infrastructure layer to clear Render's 24/7 active runtime handshake."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>PythonAnyWhere - Live Deployment Node</title>
        <style>
            body { 
                font-family: 'Courier New', Courier, monospace; 
                background-color: #050505; 
                color: #00ff33; 
                text-align: center; 
                padding-top: 15%; 
                margin: 0;
            }
            .terminal-box {
                display: inline-block;
                background-color: #000000;
                border: 2px solid #00ff33;
                padding: 40px;
                border-radius: 5px;
                box-shadow: 0 0 20px #00ff33;
            }
            h1 { font-size: 2.5em; text-transform: uppercase; letter-spacing: 2px; }
            p { font-size: 1.2em; color: #a1ffb2; }
            .credit { margin-top: 30px; font-size: 0.9em; color: #008822; }
        </style>
    </head>
    <body>
        <div class="terminal-box">
            <h1>PythonAnyWhere</h1>
            <p>CRITICAL NODE CONFIGURATION STATUS: [ONLINE 24/7]</p>
            <p>Ecosystem Pipeline Matrix Attached Successfully.</p>
            <div class="credit">Own By ShadowCraftMC, PythonAnyWhere</div>
        </div>
    </body>
    </html>
    """

def run_http_server_daemon():
    """Dynamically binds to the cloud execution port array allocated by the host system."""
    target_port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=target_port)

# ------------------------------------------------------------------------------
# 2. HACKER CONSOLE SHELL ENGINE & DATA FLOOD STREAM
# ------------------------------------------------------------------------------
def generate_hacker_ascii_banner():
    """Outputs the core brand visual frame profile straight to stdout."""
    os.system('cls' if os.name == 'nt' else 'clear')
    system_banner = """
\033[92m
 ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗██╗   ██╗██╗    ██╗██╗  ██╗███████╗██████╗ ███████╗
 ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██╔══██╗████╗  ██║╚██╗ ██╔╝██║    ██║██║  ██║██╔════╝██╔══██╗██╔════╝
 ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║███████║██╔██╗ ██║ ╚████╔╝ ██║ █╗ ██║███████║█████╗  ██████╔╝█████╗  
 ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║  ╚██╔╝  ██║███╗██║██╔══██║██╔══╝  ██╔══██╗██╔══╝  
 ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   ╚███╔███╔╝██║  ██║███████╗██║  ██║███████╗
 ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
    \033[94m[ Own By ShadowCraftMC, PythonAnyWhere ]\033[0m
    """
    print(system_banner)

def execute_infinite_matrix_stream(node_label):
    """Generates continuous fake hacker background text loop representing link pings"""
    security_payload_logs = [
        "TRACKING ENCRYPTED ROUTING LAYERS...", 
        "ESTABLISHING SECURE SSH HANDSHAKE COMPILATION...",
        "PROXY ALIAS IP TUNNEL INJECTED...", 
        "INCOMING TRAFFIC FLOW INTERCEPTED ON ZONE 9...",
        "RESOLVING CORE NETWORKING FRAMEWORK CONFIGURATIONS...", 
        "BYPASSING LOCAL SECURITY FIREWALL SUB-SYSTEMS...",
        "OVERCLOCKING CLOUD ENVIRONMENT BANDWIDTH BUFFER...", 
        "DECRYPTING ROOT SYSTEM ADMINISTRATIVE SHELL KEYS...",
        "STAGING DISCORD INTERACTIVE APP-TREE COMPONENT MATRIX...",
        "REFRESHING KEEP-ALIVE SOCKET POOL TRAFFIC STATUS..."
    ]
    print(f"\n\033[91m[!] INITIALIZATION COMPLETE: Launching 24/7 stream sequence for: {node_label}\033[0m")
    time.sleep(1.5)
    
    while True:
        formatted_log_string = f"\033[92m[SECURE_NODE_OK] {random.choice(security_payload_logs)} | Stream Segment Trace -> {node_label} | status=200 OK\033[0m"
        print(formatted_log_string)
        time.sleep(random.uniform(0.04, 0.18)) # Ultra-fast responsive console refresh index

# ------------------------------------------------------------------------------
# 3. CORE DISCORD ECOSYSTEM NODE (Pterodactyl Installation Micro-Service)
# ------------------------------------------------------------------------------
gateway_intents = discord.Intents.default()
gateway_intents.message_content = True  # Required to ensure full command synchronization access

bot_instance = commands.Bot(command_prefix='!', intents=gateway_intents, help_command=None)

@bot_instance.event
async def on_ready():
    """Fires immediately when the Discord Gateway authentication process finishes."""
    print(f"\n\033[94m[+] Discord Core Kernel Attached Seamlessly to Remote Network.\033[0m")
    print(f"\033[92m[+] Operational Identity Matrix Verified: {bot_instance.user.name}\033[0m")
    
    try:
        synchronized_commands = await bot_instance.tree.sync()
        print(f"\033[92m[+] Global Tree Sync Complete. Synced {len(synchronized_commands)} Slash Commands.\033[0m")
    except Exception as network_exception:
        print(f"\033[91m[-] Application tree sync failed: {network_exception}\033[0m")
    
    # Custom interactive status presence indicator
    await bot_instance.change_presence(activity=discord.Game(name="PythonAnyWhere by Shadow"))

@bot_instance.tree.command(
    name="make-ptero", 
    description="Make PTERODACTYL PANEL FOR FREE EASY SCRIPT BY ShadowCraftMC"
)
@app_commands.describe(description="Add any deployment strings or customization tracking notes")
async def make_ptero_command_handler(interaction: discord.Interaction, description: str):
    """Processes your unique deployment parameters and posts server scripts"""
    
    # Embedded message output blueprint
    display_embed = discord.Embed(
        title="🛠️ ShadowCraftMC System Deployment Portal",
        description=f"**Note Context Description:** {description}\n\nFollow all architectural layout instructions below to compile your private network node hosting infrastructure:",
        color=discord.Color.from_rgb(0, 255, 51) # True green hacker profile
    )
    
    display_embed.add_field(
        name="STEP 1 — PROVISION CORE SYSTEM", 
        value="`MAKE VPS FOR FREE [CMD]`\n```bash\nbash <(curl -s https://vps123.shadowcoding.qzz.io)\n```", 
        inline=False
    )
    display_embed.add_field(
        name="STEP 2 — COMPILE DEPLOYMENT PANEL", 
        value="`MAKE PTERO [CMD]`\n```bash\nbash <(curl -s https://ptero.shadowcoding.qzz.io)\n```", 
        inline=False
    )
    
    display_embed.set_footer(text="If you encounter any problems, please create a ticket #Ticket")
    
    # Combined textual output containing your exact requested strings alongside the data embed block
    await interaction.response.send_message(
        content="**HELLO, IF YOU WANT TO CREATE YOUR OWN HOSTING, THEN FOLLOW ALL THE INSTRUCTIONS**", 
        embed=display_embed
    )

# ------------------------------------------------------------------------------
# 4. SYSTEM RUNTIME ENTRY CONSOLE ROUTER
# ------------------------------------------------------------------------------
def execute_master_control_loop():
    """Manages system initialization states via an interactive console panel router."""
    generate_hacker_ascii_banner()
    print("\033[94m=== SELECT WORKSPACE ECOSYSTEM OPTION ===\033[0m")
    print("\033[92m1)\033[0m website 24/7 run (Workspace terminal keep-alive engine)")
    print("\033[92m2)\033[0m discord bot 24/7 run (Launches Pterodactyl-installer system)")
    print("\033[91m3)\033[0m Exit Console Module Framework Link\n")
    
    user_instruction_code = input("\033[93mShadowCraftMC@PythonAnyWhere:~$ \033[0m").strip()
    
    if user_instruction_code == "1":
        generate_hacker_ascii_banner()
        target_web_endpoint = input("\033[96m[paste website link and click enter to run 24/7 script]:\033[0m ").strip()
        
        if target_web_endpoint:
            # Run the Flask environment in a separate daemon thread to fulfill cloud uptime verification
            async_http_worker = Thread(target=run_http_server_daemon)
            async_http_worker.daemon = True
            async_http_worker.start()
            
            # Lock main thread loop execution directly inside infinite scrolling visualizer matrix
            execute_infinite_matrix_stream(target_web_endpoint)
        else:
            print("\033[91m[-] Empty runtime endpoint configuration string detected. Re-routing...\033[0m")
            time.sleep(2)
            execute_master_control_loop()
            
    elif user_instruction_code == "2":
        generate_hacker_ascii_banner()
        print("\033[96m[paste your bot.py file and enter to run 24/7 your discord bot]\033[0m")
        input("\033[93mPress Enter to acknowledge file staging parameters... \033[0m")
        
        # Scrapes the operating system environment register to find access token keys
        extracted_token_string = os.environ.get('DISCORD_TOKEN')
        
        if not extracted_token_string:
            print("\033[91m[-] RUNTIME CONFIGURATION NOTICE: 'DISCORD_TOKEN' environment profile missing!\033[0m")
            extracted_token_string = input("\033[95m[Manual Override] Paste Secret Discord Bot Token String:~$ \033[0m").strip()
            
        if extracted_token_string:
            # Launches background Keep-Alive Flask cluster web architecture node 
            async_http_worker = Thread(target=run_http_server_daemon)
            async_http_worker.daemon = True
            async_http_worker.start()
            
            # Offloads the Discord Bot Gateway runtime loop seamlessly into its own processor thread
            async_discord_worker = Thread(target=bot_instance.run, args=(extracted_token_string,))
            async_discord_worker.daemon = True
            async_discord_worker.start()
            
            # Prevents main process destruction by engaging the high-speed custom hacker data loop
            execute_infinite_matrix_stream("Discord-Ptero-Bot-Engine-Cluster-Online-24-7")
        else:
            print("\033[91m[-] Access parameter token missing. Execution configuration path suspended.\033[0m")
            time.sleep(2)
            execute_master_control_loop()
            
    elif user_instruction_code == "3":
        print("\033[91m[-] Disconnecting master host interface architecture. System Offline.\033[0m")
        sys.exit()
    else:
        print("\033[91m[-] Unrecognized execution terminal sequence tracking code index error.\033[0m")
        time.sleep(1.5)
        execute_master_control_loop()

if __name__ == '__main__':
    execute_master_control_loop()
