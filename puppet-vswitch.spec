%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-vswitch
%global commit e5684e5ac7f213b96d0fbc9e4efa6730730a5cbf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-vswitch
Version:        5.3.0
Release:        1%{?dist}
Summary:        A module for providing things (ports, bridges) to vSwitches (OVS)
License:        Apache-2.0

URL:            https://launchpad.net/puppet-vswitch

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
A module for providing things (ports, bridges) to vSwitches (OVS)

%prep
%setup -q -n %{name}-%{upstream_version}

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
* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 5.3.0-1
- Newton update 5.3.0 (e5684e5ac7f213b96d0fbc9e4efa6730730a5cbf)


