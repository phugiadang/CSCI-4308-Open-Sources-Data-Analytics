/*!
{
  "name": "srcset attribute",
  "property": "srcset",
  "tags": ["image"],
  "notes": [{
    "name": "Smashing Magazine Article",
    "href": "http://en.wikipedia.org/wiki/APNG"
    },{
    "name": "Generate multi-resolution images for srcset with Grunt",
    "href": "http://addyosmani.com/blog/generate-multi-resolution-images-for-srcset-with-grunt/"
    }]
}
!*/
/* DOC
Test for the srcset attribute of images
*/
define(['Modernizr', 'createElement'], function(Modernizr, createElement) {
  Modernizr.addTest('srcset', 'srcset' in createElement('img'));
});
