{
  'targets': [
    {
      'target_name': '<(module_name)',
      'sources': [
        'src/Dispatcher.h',
        'src/FixAcceptor.h',
      	'src/FixAcceptor.cpp',
        'src/FixAcceptorStartWorker.h',
      	'src/FixAcceptorStartWorker.cpp',
      	'src/FixAcceptorStopWorker.h',
      	'src/FixAcceptorStopWorker.cpp',
      	'src/FixApplication.h',
      	'src/FixApplication.cpp',
      	'src/FixConnection.h',
      	'src/FixConnection.cpp',
      	'src/FixCredentials.h',
      	'src/FixEvent.h',
      	'src/FixEventQueue.h',
        'src/FixInitiator.h',
      	'src/FixInitiator.cpp',
      	'src/FixInitiatorStartWorker.h',
      	'src/FixInitiatorStartWorker.cpp',
      	'src/FixInitiatorStopWorker.h',
      	'src/FixInitiatorStopWorker.cpp',
        'src/FixLoginProvider.h',
      	'src/FixLoginProvider.cpp',
      	'src/FixLoginResponse.h',
      	'src/FixLoginResponse.cpp',
        'src/FixLogon.h',
      	'src/FixMessageUtil.h',
      	'src/FixSendWorker.h',
      	'src/FixSendWorker.cpp',
      	'src/FixSession.h',
      	'src/FixSession.cpp',
      	'src/node_quickfix.cpp',
        'src/Threading.h',
      ],
      'link_settings': {
        'libraries': [
          '-L/usr/lib',
          '-L/usr/local/lib',
          '-L/usr/lib64',
          '-lquickfix',
          '-lpthread',
          '-lxml2',
          '-lz'
        ]
      },
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        '/usr/local/include',
        '/usr/local/include/quickfix',
        '/usr/include',
        '/usr/include/quickfix'
      ],
      'direct_dependent_settings': {
        'include_dirs': ['src']
      },
      'cflags': [ '-fexceptions', '-std=c++11' ],
      'cflags!': ['-fno-exceptions', '-fno-rtti'],
      'cflags_cc': [ '-fexceptions' ],
      'cflags_cc!': [ '-fno-exceptions', '-fno-rtti' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'GCC_ENABLE_CPP_RTTI': 'YES',
	    'OTHER_LDFLAGS': [
              '-undefined dynamic_lookup'
            ],
            "OTHER_CFLAGS": ["-mmacosx-version-min=10.7", "-stdlib=libc++"]
          }
        }]
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
