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

    def simData(self):
        q = '''
           SELECT TOP (1000) nrs.[rSchemaID]
        ,nrs.[Code]
        ,nrs.status
        ,nrs.name
        ,scc.ValidFrom
            FROM [bagsPAMF4].[dbo].[rSchema] nrs
            inner join [172.20.24.24].[bagsPAMF_CBS].[dbo].[rSchema] ors on ors.code=nrs.code
            inner join [bagsPAMF4].[dbo].rSchemaCondition scc on scc.rSchemaID = nrs.rSchemaID
            inner join [bagsPAMF4].[dbo].rSchemaParameter scp  on scc.rSchemaConditionID=scp.rSchemaConditionID

            where scc.validto is null
            and nrs.status=1
            order by nrs.code asc
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
        --and CAST(scc.ValidFrom AS datetime) = '{validfrom}'
        '''
        return q
    
    def account(self,dbname,code):
        q = f'''
            SELECT  [rTransactionTypeID]
      ,[SourceModule]
      ,[Key]
      ,[Code]
      ,[Name]
      ,[DebitCredit]
      ,[Type]
      ,[f_Active]
        FROM [{dbname}].[dbo].[rTransactionType] rtt
        where rtt.[SourceModule] = 40
        and rtt.f_active=1
        and rtt.[Code]='{code}'
        order by rtt.code asc
        '''
        return q
    
    def accuntCode(self, dbname):
        p = f'''
        SELECT 
        [Code]
        FROM [{dbname}].[dbo].[rTransactionType] rtt
        where rtt.[SourceModule] = 40
        and rtt.f_active=1
        order by rtt.code asc
        '''
        return p