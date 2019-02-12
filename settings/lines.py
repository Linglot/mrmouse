"""
{} is a placeholder, be careful with it.
I.e. in 'My name is {}' it gets changed automatically to user's name.
After each line with a placeholder there's a comment with its 'future' content.
"""
from settings.constants import GITHUB_LINK, INV_LINK

text_lines = {
    ##############  IMPORTANT  ###############
    # Hierarchy: Cog (Class) -> Method -> Line
    'voice': {
        'change':{
            'must_be_in_vc': 'You must be in a voice channel',
            'cant_edit': 'Can\'t edit that channel\'s name. ',
            'empty': 'Please enter a language',
            'shorter': 'You could use name up to 20 symbols only',
            'done': 'Language set to {}',  # Language name
        },
        'lang_were_reset': 'Channel name was reset to {}',  # Language name

        'format': '{} {} {}' # VC name, Divider, Language
    },

    # Text lines for ;who command
    'combined_search': {
        'min_max_roles_amount': 'You have to search for at least 1 role and a maximum of {}',  # Number of maximum roles
        'no_such_role': 'There\'s no **{}** role on the server',  # Role name
        'no_users_found': 'No users were found',
        'try_another_one': 'Maybe you should try another combination?',
        'x_users_for': '{} users for: {}',  # Number of users, Role list
        'one_user_for': '1 user for: {}',  # Role list
        'one_user_column_header': 'The one and only',
        'many_user_column_header': '{}-{}',  # Start number, End number
        'and_many_more': 'And {} more…'  # A number of users

        ### These are not in use for now ###
        ####################################
        # 'row_1_column': 'Total # of users',
        # 'row_2_column'
        # 'row_3_column': '☆',
        # 'row_1_column_only': 'Results are: ',  # when <6 results, this text is shown instead of 'row_1_column'
    },

    # ;lines
    'role_count': {
        'x_number_of_users': '{} users match the combination: {}',  # Total umber of users, Role list
        'one_user_in_combination': '1 user match the combination: {}',  # Role list
        'none_users_in_combination': 'No users match the combination: {}',  # Role list
        'total_in_role': 'Total in **{}**: **{}**\n'  # Role name, Number of users
    },

    # ;ping
    'mention': {
        'min_max_roles_amount': 'You have to choose for at least 1 role and a maximum of {}',  # Number of maximum roles
        'cant_ping_X': 'You can\'t ping `{}`',  # Role name
        'message': 'Hey {}',  # Pings

        # Errors
        'slow_down_m': 'You can\'t ping again for {} minutes',  # Minutes
        'slow_down_s': 'You can\'t ping again for {} seconds',  # Seconds
        'no_access': 'You don\'t have the permissions to this command'
    },

    'server_info': {
        'titles': {
            'id': 'Id',
            'owner': 'Owner',
            'region': 'Region',
            'roles': 'Roles',
            'features': 'Features',
            'default_channel': 'Default channel',
            'channels': 'Channels',
            'created_at': 'Created at',
            'members': 'Members',
            'emojis': 'Emojis'
        },
        'members_line': '{} Members, {} without any roles',  # In total, Without roles
        'x_roles': '{} roles',  # Number of roles
        'channel_line': '{} Text, {} Voice' # Text channels, Voice channels
    },

    # Text lines for ;info command
    'about': {
        'about_desc': 'Heyo! This bot was developed specially for the Linglot server. '
                      'If you have any suggestions or bug reports, please contact the server staff.',
        'about_gh_link': ':notepad_spiral: Github',
        'about_gh_desc': 'If you want to help us with our bot, or just look at our ~~crappy~~ code,'
                         'you can do it [here]({})'
            .format(GITHUB_LINK),
        'about_inv_link': ':u6708: Linguistic lot',
        'about_inv_desc': 'Here\'s an [invite link]({}) for you, if you want to join our server'
            .format(INV_LINK)
    },

    # Text lines for ;version command
    'version': {
        'version_currently': 'Current version is {}!',  # Version number
        'version_footer': 'Sincerely yours, {}'  # Bot's name
    },

    # Text lines for ;version command
    'github': {
        'github': 'Github'
    },

    # Some lines for 'oopsie' stuff
    'technical': {
        'forbidden': 'I don\'t have access to write to #{} on {}',  # Channel name, Server name
        'cant_do_in_pm': 'I can\'t perform this command in DMs',
        'none': 'None',
        'unknown_error': 'An unknown error has happened, pls report this line to the bot devs. arigato'
                         '\n\n**Copy paste this**\n`{}`'  # Error line
    },

    'logging': {
        'lang_removed': 'Language tag removed from {}',  # Channel name\
        'command_sent': '{}#{} sent \'{}\' in #{}'  # Name#0000, Command, Channel
    },
}
