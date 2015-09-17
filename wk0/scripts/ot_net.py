def net_inc_overtime(total_hours, reg_rate):
    """Calculates net pay including overtime (reg hours is 8 hrs a day)."""
    reg_hours = 8
    ot_hours = total_hours - reg_hours
    ot_rate = 1.5*reg_rate
    total_net = reg_rate*reg_hours + ot_rate*ot_hours
    return total_net

def net_reg(total_hours, reg_rate):
    """Calculates net pay without overtime"""
    net_reg = total_hours*reg_rate
    return net_reg


def net(total_hours, reg_rate):
    """Returns net pay for both normal and overtime hours in a day"""
    reg_hours = 8
    if total_hours <= reg_hours:
        return net_reg(total_hours, reg_rate)
    else: 
        return net_inc_overtime(total_hours, reg_rate)
