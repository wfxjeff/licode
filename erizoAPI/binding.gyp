{
  'targets': [
    {
      'target_name': 'addon',
      'sources': [ 'addon.cc', 'WebRtcConnection.cpp', 'OneToManyProcessor.cc' ],
      'include_dirs' : ['$(ERIZO_HOME)/src/erizo'],
      'cflags_cc' : ['-Wall', '-O3', '-g'],
      'cflags_cc!' : ['-fno-exceptions'],
      'libraries': ['-L$(ERIZO_HOME)/build/erizo', '-lerizo'],
    }
  ]
}
