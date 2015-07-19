module.exports = (grunt) ->

    static_base_path = 'site-static/'

    styles_base_path = 'style/'

    # SASS
    sass_style_path = [
        styles_base_path + 'sass/*.sass'
        styles_base_path + 'sass/**/*.sass'
    ]

    grunt.initConfig(
        pkg: grunt.file.readJSON('package.json'),

        compass:
            ####################################################################
            # DEMO SASS
            ####################################################################
            styles:
                outputStyle: 'nested',
                debugsass: true,
                options:
                    config: styles_base_path + 'config.rb',
                    sassDir: styles_base_path + 'sass',
                    cssDir: static_base_path + 'css',
                    environment: 'development'

        watch:
            styles_sass:
                files: [
                    sass_style_path
                ]

                tasks: 'compass:styles'

    )

    # npm install grunt-contrib-uglify ^grunt-contrib-coffee grunt-ngmin grunt-contrib-compass grunt-coffeedoc

    grunt.loadNpmTasks('grunt-contrib-uglify')
    grunt.loadNpmTasks('grunt-contrib-coffee')
    grunt.loadNpmTasks('grunt-contrib-compass')
    grunt.loadNpmTasks('grunt-contrib-watch')
    grunt.loadNpmTasks('grunt-coffeedoc')

    ######################
    ## SASS WATCH TASKS ##
    ######################
    grunt.registerTask('watch-styles-sass', ['watch:styles_sass'])

    grunt.registerTask('default', ['coffee', 'coffeedoc', 'uglify'])

