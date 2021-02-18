

def setTransactionStatus(obj):
    obj.TransactionNumber+=1
    row=[obj.TransactionData1,obj.TransactionItem[2]]
    if obj.BusinessRuleException:
        obj.metrics.InvalidCount+=1
        obj.metrics.SuccessCount+=1
        row.append(obj.BusinessRuleException)
    elif obj.SystemException:
        obj.metrics.FailedCount+=1
        row.append("FAILED :"+obj.SystemException)
    else:
        obj.metrics.SuccessCount+=1
        row.append("SUCCESS")
    obj.output.append(row)
        
    