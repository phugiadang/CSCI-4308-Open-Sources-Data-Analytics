'use strict';

var vlFieldDef = require('vega-lite/src/fielddef');
var vlSchemaUtil = require('vega-lite/src/schema/schemautil');
var util = require('../util');

var genEncodings = require('./encodings'),
  getMarks = require('./marks'),
  rank = require('../rank/rank'),
  consts = require('../consts');

module.exports = genSpecsFromFieldDefs;

/** Design Encodings for a set of field definition */

function genSpecsFromFieldDefs(output, fieldDefs, stats, opt, nested) {
  // opt must be augmented before being passed to genEncodings or getMarks
  opt = vlSchemaUtil.extend(opt||{}, consts.gen.encodings);
  var encodings = genEncodings([], fieldDefs, stats, opt);

  if (nested) {
    return encodings.reduce(function(dict, encoding) {
      dict[encoding] = genSpecsFromEncodings([], encoding, stats, opt);
      return dict;
    }, {});
  } else {
    return encodings.reduce(function(list, encoding) {
      return genSpecsFromEncodings(list, encoding, stats, opt);
    }, []);
  }
}

function genSpecsFromEncodings(output, encoding, stats, opt) {
  getMarks(encoding, stats, opt)
    .forEach(function(mark) {
      var spec = util.duplicate({
          // Clone config & encoding to unique objects
          encoding: encoding,
          config: opt.config
        });

      spec.mark = mark;
      // Data object is the same across charts: pass by reference
      spec.data = opt.data;

      spec = finalTouch(spec, stats, opt);
      var score = rank.encoding(spec, stats, opt);

      spec._info = score;
      output.push(spec);
    });
  return output;
}

//FIXME this should be refactors
function finalTouch(spec, stats, opt) {
  if (spec.mark === 'text' && opt.alwaysGenerateTableAsHeatmap) {
    spec.encoding.color = spec.encoding.text;
  }

  // don't include zero if stdev/mean < 0.01
  // https://github.com/uwdata/visrec/issues/69
  var encoding = spec.encoding;
  ['x', 'y'].forEach(function(channel) {
    var fieldDef = encoding[channel];

    // TODO add a parameter for this case
    if (fieldDef && vlFieldDef.isMeasure(fieldDef) && !vlFieldDef.isCount(fieldDef)) {
      var stat = stats[fieldDef.field];
      if (stat && stat.stdev / stat.mean < 0.01) {
        fieldDef.scale = {zero: false};
      }
    }
  });
  return spec;
}
