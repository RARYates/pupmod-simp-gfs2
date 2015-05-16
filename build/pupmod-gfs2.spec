Summary: gfs2 Puppet Module
Name: pupmod-gfs2
Version: 4.1.0
Release: 2
License: Apache License, Version 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: pupmod-iptables >= 4.1.0-3
Requires: pupmod-common >= 4.1.0-4
Requires: puppet >= 3.3.0
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: pupmod-gfs2-test

Prefix:"/etc/puppet/environments/simp/modules"

%description
This Puppet module provides the basic capability to configure gfs2.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/gfs2

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/gfs2
done

mkdir -p %{buildroot}/usr/share/simp/tests/modules/gfs2

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/gfs2

%files
%defattr(0640,root,puppet,0750)
/etc/puppet/environments/simp/modules/gfs2

%post
#!/bin/sh

if [ -d /etc/puppet/environments/simp/modules/gfs2/plugins ]; then
  /bin/mv /etc/puppet/environments/simp/modules/gfs2/plugins /etc/puppet/environments/simp/modules/gfs2/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-2
- Changed puppet-server requirement to puppet

* Fri Apr 04 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-1
- Added an acpid service that is both stopped and disabled so that gfs2 works
  properly. This will actively conflict with the acpid module but that is
  appropriate since both should not be included in the same system.

* Fri Feb 28 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-0
- Updated for puppet 3 and hiera.
- Added basic spec tests for test coverage and completeness.

* Wed Oct 02 2013 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-5
- Use 'versioncmp' for all version comparisons.

* Wed Apr 11 2012 Maintenance
2.0.0-4
- Moved mit-tests to /usr/share/simp...
- Updated pp files to better meet Puppet's recommended style guide.

* Fri Mar 02 2012 Maintenance
2.0.0-3
- Improved test stubs.

* Mon Dec 26 2011 Maintenance
2.0.0-2
- Updated the spec file to not require a separate file list.

* Mon Oct 10 2011 Maintenance
2.0.0-1
- Updated to put quotes around everything that need it in a comparison
  statement so that puppet > 2.5 doesn't explode with an undef error.

* Tue Jan 11 2011 Maintenance
2.0.0-0
- Refactored for SIMP-2.0.0-alpha release

* Tue Oct 26 2010 Maintenance - 1-1
- Converting all spec files to check for directories prior to copy.

* Fri May 21 2010 Maintenance
1.0-0
- Code refactor and doc update..

* Tue Nov 24 2009 Maintenance
0.1-3
- Blocked out the previously necessary rgmanager ports.
- These are no longer necessary as of RHEL 5.2
- Also added an IPTables rule allowing multicast from 224.0.0.1 for the cluster
  software.

* Mon Nov 02 2009 Maintenance
0.1-2
- Added the sg3_utils package for proper SCSI fencing.

* Tue Oct 06 2009 Maintenance
0.1-1
- Wrapped the iptables rules in defines and the acpid segment in an 'if'
  statement using the common::has_service_acpid fact.
- Also removed kmod-cmirror since it appears to have gone away.

* Tue Sep 29 2009 Maintenance
0.1-0
- Initial configuration module
