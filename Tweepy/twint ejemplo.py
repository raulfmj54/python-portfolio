import twint



# Configure
c = twint.Config()

c.Search = "hugo_app"

# Run
twint.run.Search(c)