# Authorization 
* In the HTTP request header, include the token key in this form (note the whitespace after 'Token')

`Authorization: Token be1314c3be8264b2f3b1a46de5fb9e05ef4e9808`

# POST /api/tournaments
* The JSON body should match the form below, with `is_judge` indicating whether the tournament creator wishes to join
  as a judge.
```
{
	"name": "Biggest Pasta Tournament",
	"start_date": "2019-07-29 21:51:23+00",
	"creator": 2,
	"users":
		[{
            "is_judge": false
        }]
}
```