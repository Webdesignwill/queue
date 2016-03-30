"use strict";

var gulp = require('gulp'),
  uglify = require('gulp-uglify'),
  jshint = require('gulp-jshint'),
  webserver = require('gulp-webserver'),
  cssmin = require('gulp-cssmin'),
  path = require('path');

var environment = process.env.NODE_ENV || "development",
      serverRoot = environment === "production" ? "dist" : "public",
      serverPort = environment === "production" ? 9000 : 8080;

gulp.task('jsmin', function() {
  gulp.src('public/js/**/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('dist/js'));
});

gulp.task('cssmin', function () {
  gulp.src('public/css/**/*.css').pipe(cssmin()).pipe(gulp.dest('dist/css'));
});

gulp.task('copy-index-html', function () {
  return gulp.src('public/index.html')
    .pipe(gulp.dest('dist'));
});

gulp.task('copy-img', function () {
  return gulp.src('public/img/**/*')
    .pipe(gulp.dest('dist/img'));
});

gulp.task('webserver', function() {
  gulp.src(serverRoot).pipe(webserver({
    port: serverPort,
    livereload: false,
    directoryListing: {
      enable: false
    },
    open: false
  }));
});

gulp.task('build', [
  'copy-index-html',
  'jsmin',
  'cssmin',
  'webserver'
]);

gulp.task('default', ['webserver']);