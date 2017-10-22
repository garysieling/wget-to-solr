curl "http://40.87.64.225:8983/solr/glass/update?commit=true" -H "Content-Type: text/xml" --data-binary '<delete><query>*:*</query></delete>'
