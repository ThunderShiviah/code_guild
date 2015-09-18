
def net(total_hours, reg_rate):
    """Returns net pay for both normal and overtime hours in a day.
    
    Parameters
    ----------
    total_hours: int 
    The total hours worked during a single work day.
    
    reg_rate: int
    The standard (non-overtime) hourly wage."""
    

    reg_hours = 8 # Max daily hours before overtime.
    
    assert total_hours >= 0 # We shouldn't have negative worked hours.
    assert reg_rate >= 0 # Pay rate should not be negative

    def net_inc_overtime():
        """Calculates net pay including overtime (reg hours is 8 hrs a day)."""

        ot_hours = total_hours - reg_hours
        ot_rate = 1.5*reg_rate # Overtime pay is time and a half (hence the 1.5).
        total_net = reg_rate*reg_hours + ot_rate*ot_hours
        return total_net

    def net_reg():
        """Calculates net pay without overtime"""
        net_reg = total_hours*reg_rate
        return net_reg


    if total_hours <= reg_hours:
        return net_reg()
    else: 
        return net_inc_overtime()
