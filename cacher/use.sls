qvm-present-id:
  qvm.present:
    - name: cacher
    - template: template-cacher
    - label: gray

/etc/qubes/policy.d/50-config-updates.policy:
  file.prepend:
    - header: True
    - text:
      - "qubes.UpdatesProxy  *  @tag:whonix-updatevm  @default  allow target=sys-whonix"
      - "qubes.UpdatesProxy  *  @tag:whonix-updatevm  @anyvm    deny"
      - "qubes.UpdatesProxy  *  @type:TemplateVM      @default  allow target=cacher"
