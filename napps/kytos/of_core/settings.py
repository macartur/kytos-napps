"""Settings for the of_core NApp.."""
#: Pooling frequency
STATS_INTERVAL = 5

#: Supported Versions
OPENFLOW_VERSIONS = [0x01, 0x04]

#: If SEND_FEATURES_REQUEST_ON_ECHO is True, kytos/of_core must send
#: FeaturesRequest when when it sends an echo reply message
SEND_FEATURES_REQUEST_ON_ECHO = False
