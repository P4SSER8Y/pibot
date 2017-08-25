def msgbox(title, message, timeout=3):
    import rospy
    from pibot import srv

    f = rospy.ServiceProxy('/pibot/screens/srv_msgbox', srv.msgbox)
    req = srv.msgboxRequest()
    req.timeout = timeout
    req.message = '{0:-^16}\n{1:^16}'.format(title[:16], message)
    try:
        return f(req)
    except Exception:
        return False

