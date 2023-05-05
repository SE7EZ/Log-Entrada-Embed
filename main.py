@client.event
async def on_member_join(member):
    # Define o canal de boas-vindas
    channel = client.get_channel(1234567890) # Substitua pelo ID do canal de boas-vindas do seu servidor
    
    # Cria um embed de boas-vindas personalizado
    embed = discord.Embed(
        title=f"Bem-vindo ao servidor, {member.name}!",
        description=f"Leia as regras em <#1234567891> e apresente-se em <#1234567892> para conhecer a comunidade!",
        color=discord.Color.green()
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"ID do usuário: {member.id}")
    
    # Envia a mensagem de boas-vindas para o canal de boas-vindas
    await channel.send(embed=embed)
    
    # Define o cargo de boas-vindas para o novo membro
    role = discord.utils.get(member.guild.roles, name="Membro")
    await member.add_roles(role)
