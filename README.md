<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <!-- viewport meta tag for device compatibility -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Mission to Mars</title>
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js">
    </script>
  </head>
  <body>
    <div class = "bg" style="background-color:#daa26e">
      <div class="container">        
        <div class="col-md-12">
            <!-- Add Jumbotron to Header -->
            <div class="jumbotron text-center" style="background-color:#db8a3e">
              <h1>Mission to Mars</h1>
            <!-- Add a button to activate scraping script -->
              <p><a class="btn btn-warning btn-lg active" href="/scrape" role="button">Scrape New Data</a></p>
        </div>
      </div>
    
        <!-- Add section for Mars News -->
      <div class="container">
        <div class="row" id="mars-news">
          <div class="col-md-12">
            <div class="media">
              <div class="media-body">
                <h2>Latest Mars News</h2>
                  <div class="jumbotron"   
                   style="background-color:#db8a3e">
                  <h4 class="media-heading">{{ mars.news_title }}</h4>
                  <p>{{ mars.news_paragraph }}</p>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>
        <!-- Section for Featured Image and Facts table -->
        <div class="row" id="mars-featured-image">
          <div class="col-xs-12 col-md-8">
            <h2>Featured Mars Image</h2>
            <!-- if images is False/None/non-existent, then default to error message -->
            <img
              src="{{mars.featured_image | default('static/images/error.png', true) }}"
              class="img-responsive"
              alt="Responsive image"
            />
          </div>

          <div class=" col-xs-12 col-md-4">
            <!-- Mars Facts -->
            <div class="row" id="mars-facts">
              <h4>Mars Facts</h4>
              {{ mars.facts | safe }}
            </div>
          </div>
        </div>

        <!-- Section for Mars Hemispheres -->
        <div class="row" id="mars-hemispheres">
          <div class="page-header">
            <h2 class="text-center">Mars Hemispheres</h2>
          </div>

          {% for hemisphere in mars.hemispheres %}
          <div class="col-xs-6 col-md-6">
            <div class="thumbnail">
              <img src="{{hemisphere.img_url | default('static/images/error.png', true)}}" alt="...">
              <div class="caption">
                <h3>{{hemisphere.title}}</h3>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </body>
</html>
