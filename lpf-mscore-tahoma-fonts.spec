# %%global will not work here, lazy evaluation needed.
%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-mscore-tahoma-fonts
Version:        1.0
Release:        2%{?dist}
Summary:        Bootstrap package building mscore-tahoma-fonts using lpf

License:        MIT
URL:            https://github.com/leamas/lpf
Group:          Development/Tools
BuildArch:      noarch
Source0:        mscore-tahoma-fonts.spec.in
Source1:        License.txt
Source2:        61-mscore-tahoma.conf


BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf


%description
Bootstrap package allowing the lpf system to build the
mscore-tahoma-fonts non-redistributable package.


%prep
%setup -cT


%build


%install
# lpf-setup-pkg [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg -e %{SOURCE1} %{buildroot} %{SOURCE0} \
    %{SOURCE2}


%post
%lpf_post

%postun
%lpf_postun

%lpf_triggerpostun


%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}


%changelog
* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 14 2014 Alec Leamas <leamas.alec@gmail.com> - 1.0-1
- Changed description, downplaying usefullness.
- Lowered config priority (55 -> 61).

* Mon Feb 10 2014 Alec Leamas <leamas@nowhere.net> - 1.0-1
- Initial release
