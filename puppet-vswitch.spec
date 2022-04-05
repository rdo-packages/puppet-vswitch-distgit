%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-vswitch
Version:        16.3.0
Release:        1%{?dist}
Summary:        A module for providing things (ports, bridges) to vSwitches (OVS)
License:        ASL 2.0

URL:            https://launchpad.net/puppet-vswitch

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet >= 2.7.0
Requires:       puppet-openstacklib >= 19.1.0
Requires:       puppet-stdlib       >= 5.0.0
Requires:       puppet-kmod

%description
A module for providing things (ports, bridges) to vSwitches (OVS)

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Tue Apr 05 2022 RDO <dev@lists.rdoproject.org> 16.3.0-1
- Update to 16.3.0



