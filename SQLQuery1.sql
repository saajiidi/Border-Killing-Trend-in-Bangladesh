create database bdkillinc

Select *
From dbo.border_incidents



Select Killed, YEAR, Rulling_Party
From border_incidents
Where Killed > (Select avg(Killed)
				From border_incidents)

Select avg(killed)
From border_incidents

UPDATE border_incidents
SET  Rulling_Party = 'BNP'
Where (1990 < Year And Year < 1997) OR (2000 < Year And Year < 2007) OR (1978 < Year And Year < 1982)

UPDATE border_incidents
SET  Rulling_Party = 'BAL'
Where (1996 < Year And Year < 2001) OR (2008 < Year) OR (1971 < Year And Year < 1976)

UPDATE border_incidents
SET  Rulling_Party = 'others'
Where Rulling_Party is Null


Select avg(killed)
From border_incidents
Where Rulling_Party= 'BNP'

Select avg(killed)
From border_incidents
Where Rulling_Party= 'BAL'

Select avg(killed)
From border_incidents
Where Rulling_Party= 'others'

Select avg(killed)
From border_incidents
Where Rulling_Party_India= 'BJP'

Select avg(killed)
From border_incidents
Where Rulling_Party_India= 'Congress'

Select avg(killed)
From border_incidents
Where Rulling_Party_India= 'others'



Select avg(Rape)
From border_incidents
Where Year > 1999 AND Rulling_Party= 'BNP'

Select avg(Rape)
From border_incidents
Where Year > 1999 AND Rulling_Party= 'others'

Select sum(Killed)
From border_incidents
Where Year > 2001 AND Year < 2013

Select sum(Injured)
From border_incidents
Where Year > 2001 AND Year < 2013

Select sum(Killed)
From border_incidents
Where Year > 2010 

Select *
From border_incidents
Where Year > 1999 

Select avg(Missing)
From border_incidents
Where Year > 1999 AND Rulling_Party= 'BNP'

Select avg(Rape)
From border_incidents
Where Year > 1999 AND Rulling_Party= 'others'


ALTER TABLE border_incidents
ADD Rulling_Party_India varchar(255);

UPDATE border_incidents
SET  Rulling_Party_India = 'BJP'
Where Year > 1976 and Year < 1980 OR Year > 1997 and Year < 2004 OR Year > 2013

UPDATE border_incidents
SET  Rulling_Party_India = 'others'
Where Year > 1989 and Year < 1991 OR Year > 1995 and Year < 1998 