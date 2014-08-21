{
  'variables': {
    'component': 'static_library',
    'disable_nacl': 1,
    'enable_printing': 0,
    'linux_use_bundled_binutils': 0,
    'linux_use_bundled_gold': 0,
    'linux_use_gold_flags': 0,
    'remoting': 0,
    'use_cups': 0,
    'use_gio': 0,
    'use_gnome_keyring': 0,
    'use_kerberos': 0,
    'use_system_expat': 1,
    'use_system_flac': 1,
    'use_system_fontconfig': 1,
    'use_system_harfbuzz': 1,
    'use_system_icu': 1,
    'use_system_libevent': 1,
    'use_system_libjpeg': 1,
    'use_system_libpng': 1,
    'use_system_libusb': 1,
    'use_system_libxslt': 1,
    'use_system_openssl': 1,
    'use_system_speex': 1,
    'use_system_zlib': 1,
    'chromeos': 0,
    'embedded': 1,
    'ozone_platform_gbm': 1,
    'use_ozone': 1,
    'use_udev': 1,
  },
  'target_defaults': {
    'ldflags!': [
      '-Wl,--fatal-warnings',
    ],
  },
}
