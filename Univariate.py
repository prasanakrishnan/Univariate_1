class Univariate():
    def QualQuan(dataset):
        Qual=[]
        Quan=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=="O"):
                #print('Qual')
                Qual.append(columnName)
            else:
                #print('Quan')
                Quan.append(columnName)
        return Qual,Quan
    
    def FreqTable(columnName,dataset):
        FreqTable=pd.DataFrame(columns=['Unique_Value','Frequency','Relative_Frequency','cumsum'])
        FreqTable['Unique_Value']=dataset[columnName].value_counts().index
        FreqTable['Frequency']=dataset[columnName].value_counts().values
        FreqTable['Relative_Frequency']=(FreqTable['Frequency']/103)
        FreqTable['cumsum']=FreqTable['Relative_Frequency'].cumsum()
        return FreqTable
    
     def Univarite(dataset,Quan):
                                                                                                                                                    descriptive=pd.DataFrame(index=['mean','median','mode','Q1:25%','Q2:50%','Q3:75%','99%','Q4:100%','IQR','1.5                                                  rule','Lesser','Greater','min','max'],columns=Quan)
                
        for columnName in Quan:
            descriptive[columnName]['mean']=dataset[columnName].mean()
            descriptive[columnName]['median']=dataset[columnName].median()
            descriptive[columnName]['mode']=dataset[columnName].mode()[0]
            descriptive[columnName]['Q1:25%']=dataset.describe()[columnName]['25%']
            descriptive[columnName]['Q2:50%']=dataset.describe()[columnName]['50%']
            descriptive[columnName]['Q3:75%']=dataset.describe()[columnName]['75%']
            descriptive[columnName]['99%']=np.percentile(dataset[columnName],99)
            descriptive[columnName]['Q4:100%']=dataset.describe()[columnName]['max']
            descriptive[columnName]['IQR']=descriptive[columnName]['Q3:75%']-descriptive[columnName]['Q1:25%']
            descriptive[columnName]['1.5 rule']=1.5*descriptive[columnName]['IQR']
            descriptive[columnName]['Lesser']=descriptive[columnName]['Q1:25%']- descriptive[columnName]['1.5 rule']
            descriptive[columnName]['Greater']=descriptive[columnName]['Q3:75%']+descriptive[columnName]['1.5 rule']
            descriptive[columnName]['min']=dataset[columnName].min()
            descriptive[columnName]['max']=dataset[columnName].max()
        return descriptive

    
    def Outlier_columnName(dataset):
        descriptive ['hsc_p']['min']<descriptive['hsc_p']['Lesser']
        Lesser=[]
        Greater=[]
        for columnName in Quan:
            if(descriptive [columnName]['min']<descriptive[columnName]['Lesser']):
                Lesser.append(columnName)
            if(descriptive [columnName]['max']>descriptive[columnName]['Greater']):
                Greater.append(columnName)
        return Lesser,Greater
    
    def Replacing_outlier(dataset):
        Lesser=[]
        Greater=[]
        for columnName in Quan:
            if(descriptive [columnName]['min']<descriptive[columnName]['Lesser']):
                Lesser.append(columnName)
            if(descriptive [columnName]['max']>descriptive[columnName]['Greater']):Greater.append(columnName)
        return Lesser,Greater



