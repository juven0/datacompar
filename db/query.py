class Query:
    def __init__(self) -> None:
        pass

    def getSchemaName(self, dbname):
        q = f'''
        SELECT  sc.rSchemaID
            ,[Code]
            ,[Name]
            ,[Status]
            ,[Key]
            ,[ValidTo]
            ,scc.ValidFrom
            ,scp.rSchemaParameterID
            ,sccb.*
        FROM [{dbname}].[dbo].[rSchema] sc
        inner join [{dbname}].[dbo].rSchemaCondition scc on scc.rSchemaID = sc.rSchemaID
        inner join [{dbname}].[dbo].rSchemaParameter scp  on scc.rSchemaConditionID=scp.rSchemaConditionID
        inner join [{dbname}].[dbo].rSchemaCombination sccb on sccb.rSchemaConditionID=scc.rSchemaConditionID


        where sc.Status=1
        and scc.validto is null
        '''
        return q
    
    def getgetSchemaByName(self, dbname, name, validfrom):
        validfrom = validfrom.strip(" '")
        q = f'''
        SELECT  sc.rSchemaID
            ,[Code]
            ,[Name]
            ,[Status]
            ,[Key]
            ,[ValidTo]
            ,scc.ValidFrom
            ,scp.rSchemaParameterID
            ,sccb.*
        FROM [{dbname}].[dbo].[rSchema] sc
        inner join [{dbname}].[dbo].rSchemaCondition scc on scc.rSchemaID = sc.rSchemaID
        inner join [{dbname}].[dbo].rSchemaParameter scp  on scc.rSchemaConditionID=scp.rSchemaConditionID
        inner join [{dbname}].[dbo].rSchemaCombination sccb on sccb.rSchemaConditionID=scc.rSchemaConditionID


        where sc.Status=1
        and scc.validto is null
        and sc.Name='{name}'
        and CAST(scc.ValidFrom AS datetime) = '{validfrom}'
        '''
        return q
