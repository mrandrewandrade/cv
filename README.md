# Databased Portfolio and Curriculum Vitae  

Online curriculum vitae and porfolio optimized for researchers who strive for a minimalistic, file based content management system. 

The site is based on a json/xml file (ie ```projects.json```,  ```awards.json```, etc.)  per section (ie ```projects.html```) which generates the content on the site based on _layout.  

##Features:
* fully responsive, single scrolling page design
* provides various layouts for different section
* content is loaded from json files (_data)
* each section has it own html file (_includes)
* php free contact form using [Formspree](http://formspree.io/)
* optimized for [Github Pages'](https://pages.github.com/) deployment
* favors beautiful html output over jekyll code formatting 
* simple source code and structure that can be modified or extended easily
* yields valid html5

##Dependencies:
* [Jekyll](http://jekyllrb.com/)    
* [spin.js](http://fgnass.github.io/spin.js/)    

##Usage
To run locally:
First install [Jekyll](http://jekyllrb.com/).  This requires both [Ruby on Rails](http://rubyonrails.org/) and [Node.js](https://nodejs.org/)

Then clone the repo and run:       
  bundle install    
  
After ther equired gems are installed, run:     
  jekyll Serve     

### Enjoy!
