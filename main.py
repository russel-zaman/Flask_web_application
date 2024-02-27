from website import create_app

app = create_app()

if __name__ == "__main__":          # only if we run this file directly , not when importing it in another project 
    app.run(debug=True)             # this line ecxecute and run the application
                                    # debug = True means; if we change in our python code it is going to rerun the web server
    