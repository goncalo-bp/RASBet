from DBQueries import DBQueries
import datetime

dbq = DBQueries()

dbq.registerUser("a","a@gm.com","teste","123782",datetime.date(2000,1,1),0,0)
#dbq.setResultado("Draw","6ae5f22198593f180590bf8161bbf910")
#dbq.setResultado("Draw","72cdea24cebb5465e577b8fe3f3cdfeb")
#print(dbq.criarAposta("1",5,[('6ae5f22198593f180590bf8161bbf910','Vitória SC')]))
#print(dbq.criarAposta("1",5,[('6ae5f22198593f180590bf8161bbf910','Draw')]))
#dbq.criarAposta("1",5,[('6ae5f22198593f180590bf8161bbf910','Vitória SC'),('72cdea24cebb5465e577b8fe3f3cdfeb','Boavista Porto')])
#dbq.criarAposta("1",5,[('6ae5f22198593f180590bf8161bbf910','Draw'),('72cdea24cebb5465e577b8fe3f3cdfeb','Boavista Porto')])
#print(dbq.criarAposta("1",5,[('6ae5f22198593f180590bf8161bbf910','Draw'),('72cdea24cebb5465e577b8fe3f3cdfeb','Draw')]))
dbq.registerSpecialUser("b","b@gm.com","b",1,0)
dbq.registerSpecialUser("c","c@gm.com","c",0,1)

#dbq.datasDisponiveis('Futebol')

#dbq.jogoPorData(datetime.date(2022,11,6),'Futebol')



#dbq.criarAposta("1",20,[('B','Draw')])
#dbq.atualizaResultadoApostas('6ae5f22198593f180590bf8161bbf910','Vitória SC')
#dbq.atualizaResultadoApostas('72cdea24cebb5465e577b8fe3f3cdfeb','Boavista Porto')
