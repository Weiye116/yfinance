select t1.Company_name, t1.Hour, t2.ts as Datetime_high, t1.Highest_hourly_price, t1.Lowest_hourly_price
from (
    select name as Company_name, (extract(hour from (cast(ts as timestamp)))- 4) as Hour,
    max(high) as Highest_hourly_price, min(low) as Lowest_hourly_price
    from  "finance-database"."00"
    group BY name,(extract(hour from (cast(ts as timestamp))) - 4)
    order BY name,(extract(hour from (cast(ts as timestamp))) - 4)
     ) t1,
  "finance-database"."00" t2

where t1.Company_name=t2.name 
and t1.Hour = (extract(hour from (cast(ts as timestamp))) - 4) 
and t1.Highest_hourly_price = t2.high;