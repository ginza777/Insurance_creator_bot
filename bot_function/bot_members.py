# from botapp.management.commands.bot import *
# from botapp.models import Profile,Group_members
# from telegram import ChatAction
# def new_member(update, context):
#     chat_id = update.message.chat_id
#     print(chat_id)
#     new_members = update.message.new_chat_members
#     added_by = update.message.from_user
#     if added_by:
#         print(added_by)
#         added_by_id = added_by.id
#         status='byuser'
#
#
#
#     for member in new_members:
#         # Send a welcome message to each new member
#         update.message.reply_text(f"Welcome to the group, {member.first_name}!")
#         print(member.id,member.first_name,member.last_name,member.username,member.is_bot,member.language_code)
#         print(member)
#         if added_by.id == member.id:
#             status='shaxsiy'
#
#         id= member.id
#         f_name= member.first_name
#         l_name= member.last_name
#         username= member.username
#         is_bot= member.is_bot
#         language_code= member.language_code
#
#
#         try:
#             member = Group_members.objects.get(exeterenal_id=id)
#             member.InvitedUserId = added_by_id,
#             member.group_id = chat_id,
#             member.exeterenal_id = id,
#             member.f_name = f_name,
#             member.l_name = l_name,
#             member.username = username,
#             member.is_bot = is_bot,
#             member.language_code = language_code,
#             member.invited_status = status,
#
#             print("gruppaga qo'shilgan  bazadan yangilandi")
#
#         except:
#
#             Group_members.objects.create(
#                 InvitedUserId=added_by_id,
#                 group_id=chat_id,
#                 exeterenal_id=id,
#                 f_name=f_name,
#                 l_name=l_name,
#                 username=username,
#                 is_bot=is_bot,
#                 language_code=language_code,
#                 invited_status=status,
#
#
#             )
#
#             print("gruppaga qo'shilgan  bazaga qo'shildi")
#
#
#
#
