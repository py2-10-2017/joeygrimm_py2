select date_format(billing.charged_datetime, '%m') as 'month', date_format(billing.charged_datetime, '%y') as 'year', sum(amount) as total_revenue
from billing
where month(billing.charged_datetime) = 3 and year(billing.charged_datetime) = 2012;


select billing.client_id, sum(amount) as total_revenue
from billing
where billing.client_id = 2;

select sites.domain_name as client_10_domains
from sites
where sites.client_id = 10;

select sites.client_id, count(sites.site_id) as number_of_sites , date_format(sites.created_datetime, '%m') as per_month, date_format(sites.created_datetime, '%y') as per_year
from sites
where sites.client_id = 1 
group by per_month, per_year
order by per_year desc;

select sites.client_id, count(sites.site_id) as number_of_sites , date_format(sites.created_datetime, '%m') as per_month, date_format(sites.created_datetime, '%y') as per_year
from sites
where sites.client_id = 20 
group by per_month, per_year
order by per_year desc;

select sites.domain_name, count(leads.leads_id) as number_of_leads, date_format(leads.registered_datetime, '%d') as 'day', date_format(leads.registered_datetime, '%m') as 'month', date_format(leads.registered_datetime, '%y') as 'year'
from sites
left join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-02-15'
group by sites.site_id;	

select clients.client_id, concat(clients.first_name, ' ', clients.last_name) as 'name', count(leads.leads_id) as 'total leads for 2011'
from clients
left join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by clients.client_id asc;

select clients.client_id, concat(clients.first_name, ' ', clients.last_name) as 'name', date_format(leads.registered_datetime, '%m') as 'Month', count(leads.leads_id) as 'monthly leads'
from clients
left join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-06-31'
group by clients.client_id, month(leads.registered_datetime)
order by month(leads.registered_datetime);

select clients.client_id, concat(clients.first_name, ' ', clients.last_name) as 'name', sites.domain_name, count(leads.leads_id) as 'number of leads', date_format(leads.registered_datetime, '%M %d, %Y') as 'genreated date'
from clients
join sites on clients.client_id = sites.client_id
left join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by sites.domain_name
order by clients.client_id;


select clients.client_id, concat(clients.first_name, ' ', clients.last_name) as 'name', sites.domain_name, count(leads.leads_id) as 'number of leads'
from clients
join sites on clients.client_id = sites.client_id
left join leads on sites.site_id = leads.site_id
group by clients.client_id, sites.domain_name;



select clients.client_id, concat(clients.first_name, ' ', clients.last_name) as 'name', sum(billing.amount) as 'monthly revenue', date_format(billing.charged_datetime, '%M') as 'month', DATE_FORMAT(billing.charged_datetime, '%Y') as 'year'
from clients
left join billing on clients.client_id = billing.client_id
group by 'name' , month(billing.charged_datetime), year(billing.charged_datetime)
order by clients.client_id;


select clients.client_id, concat(clients.first_name, ' ', clients.last_name) as 'name', group_concat(sites.domain_name) as 'websites'
from clients
left join sites on clients.client_id = sites.client_id
group by clients.client_id;

