Name:           gespeaker
Version:        0.8.1
Release:        1%{?dist}
Summary:        A GTK+ frontend for eSpeak and mbrola

Group:          Applications/Multimedia
License:        GPLv2
URL:            http://code.google.com/p/gespeaker/
Source0:        http://gespeaker.googlecode.com/files/gespeaker_%{version}_all.tar.gz

BuildRequires:  python >= 2.4 , python-setuptools , gettext
Requires:       espeak , pygtk2-libglade , gnome-python2-rsvg

%description
Gespeaker is a GTK+ frontend for espeak. It allows to play a text in many 
languages with settings for voice, pitch, volume, speed and word gap. The 
text played can also be recorded to WAV file.
Since version 0.6 it supports mbrola voices, it will require mbrola package 
and one or more mbrola voices from Debian repository or Ubuntu Trucchi 
repository.

Multiple languages are supported, currently English, Italian, French and 
Spanish. It works well with both Gnome, XFCE, LXDE environments.

%prep
%setup -q

%build
python setup.py build


%install
python setup.py install --root %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/locale/*
%{python_sitelib}/*.egg-info
%doc
%{_defaultdocdir}/%{name}/*
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun Jul 24 2011 Raphael Groner raphgro-at-web.de - 0.8.1-1
- Initial version

