def format_users(usersRaw):
    users = []
    for item in usersRaw.items:
        print(item.genderData.value)
        user = format_user(item)
        users.append(user)
    return users


def format_user(userRaw):
    return {
        "id": userRaw.id,
        "fullName": userRaw.fullName,
        "genderID": userRaw.genderID,
        "address": userRaw.address,
        "phonenumber": userRaw.phonenumber,
        "email": userRaw.email,
        "roleID": userRaw.roleID,
        "gender_value": userRaw.genderData.value,
        "role_value": userRaw.roleData.value,
    }
