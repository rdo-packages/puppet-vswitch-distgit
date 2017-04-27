%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-vswitch
Version:        6.3.1
Release:        1%{?dist}
Summary:        A module for providing things (ports, bridges) to vSwitches (OVS)
License:        ASL 2.0

URL:            https://launchpad.net/puppet-vswitch

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
A module for providing things (ports, bridges) to vSwitches (OVS)

%prep
%setup -q -n openstack-vswitch-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/vswitch/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/vswitch/



%files
%{_datadir}/openstack-puppet/modules/vswitch/


%changelog
* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 6.3.1-1
- Update to 6.3.1

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 6.3.0-1
- Update to 6.3.0


