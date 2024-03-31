Name:           3isec-qubes-sys-multimedia
Version:       	2.3
Release:        3%{?dist}
Summary:        creates multimedia template and qubes

License:        GPLv3+
SOURCE0:       	multimedia
Requires:       3isec-qubes-common

%description
 This package sets up qubes to work mith multimedia files in Qubes.
 By default a qube named "media" is created, and configured so that any
 multimedia files are opened in a named disposable called "multimedia".
 This provides some measure of protection when working with untrusted files.

The media qube is offline by default.
The multimedia disposable is offline by default.
You can change this if you wish, but be aware that this may result in
data leakage.

The idea is that you organise and store media files in the media qube. 
Opening a file in that qube will open the multimedia disposable and play
the file there.
You can also use the multimedia disposable from any other qube, or use the
disposable template to create more disposables with different settings -
perhaps online, or restricted to certain IP addresses.
Access to the multimedia file is controlled from the policy file in
/etc/qubes/policy.d/30-user.policy



%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/salt
cp -rv %{SOURCE0}/  %{buildroot}/srv/salt

%files
%defattr(-,root,root,-)
/srv/salt/multimedia/*

%post
if [ $1 -eq 1 ]; then
  qubesctl state.apply multimedia.clone
  qubesctl --skip-dom0 --targets=template-multimedia state.apply multimedia.install
  qubesctl state.apply multimedia.create
  qubesctl --skip-dom0 --targets=media state.apply 3isec-common.store.install
  qubesctl --skip-dom0 --targets=media state.apply multimedia.configure
fi
if [ $1 -eq 2 ]; then
  qubesctl --skip-dom0 --targets=media state.apply multimedia.configure
fi

%changelog
* Sun Mar 31 2024 unman <unman@thirdeyesecurity.org> - 2.3.3
- Make call to disposable-open view-only
* Fri Mar 15 2024 unman <unman@thirdeyesecurity.org> - 2.3.2
- Use 3isec-common for thunar install
* Tue Feb 13 2024 unman <unman@thirdeyesecurity.org> - 2.3
- Use template-store with thunar for media qube
* Mon Feb 20 2023 unman <unman@thirdeyesecurity.org> - 2.2
- Use pillar for cacher to determine repo changes
* Sat May 21 2022 unman <unman@thirdeyesecurity.org> - 2.1
- Standardise package names to 3isec-
* Sun May 15 2022 unman <unman@thirdeyesecurity.org> - 2.0
- Add post install salting
* Wed Feb 03 2021 unman <unman@thirdeyesecurity.org>
- First Build
